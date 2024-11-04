export function isLocalMode() {
  return !window.pywebview && !localStorage.getItem("dcalc/access_token")
}
