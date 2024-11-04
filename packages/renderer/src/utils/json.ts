export function safeParse(json: string | null, defaultValue?: any) {
  if (json == null) {
    return defaultValue ?? null
  }
  if (json == "") {
    return defaultValue ?? ""
  }
  try {
    return JSON.parse(json)
  } catch (e) {
    return defaultValue ?? null
  }
}
