"""Application factory."""
import os
from flask import Flask, render_template
from config import Config
from .extensions import db, migrate, login_manager, csrf

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    os.makedirs(app.instance_path, exist_ok=True)  # DB folder must exist

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "shop.home"  # becomes auth.login in Milestone 3

    @login_manager.user_loader
    def load_user(user_id):
        return None

    csrf.init_app(app)

    from .shop import bp as shop_bp
    app.register_blueprint(shop_bp)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        db.session.rollback()
        return render_template("500.html"), 500

    return app