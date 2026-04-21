export function resolveTeleportTarget(target?: string | Element | null) {
  if (typeof window === 'undefined') {
    return null
  }

  if (typeof target === 'string') {
    return document.querySelector(target)
  }

  return target ?? document.body
}

export function getElementZoom(target?: string | Element | null) {
  if (typeof window === 'undefined') {
    return 1
  }

  let zoom = 1
  let current = resolveTeleportTarget(target) as HTMLElement | null

  while (current) {
    const currentZoom = Number.parseFloat(window.getComputedStyle(current).zoom)

    if (Number.isFinite(currentZoom) && currentZoom > 0) {
      zoom *= currentZoom
    }

    current = current.parentElement
  }

  return zoom || 1
}
