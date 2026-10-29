// Shared behaviour. Cart logic goes in cart.js (Milestone 5).
document.querySelectorAll('[data-fb-dismiss]').forEach(function (el) {
  setTimeout(function () { el.remove(); }, 5000);
});
