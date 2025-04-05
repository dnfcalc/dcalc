interface Number {
  plus(value: number): number

  minus(value: number): number

  multiply(value: number): number

  divide(value: number): number

  perMulti(value: number): number

  round(digit?: number): number

  floor(digit?: number): number

  exactlyDivide(value: number): number
}

interface Array<T> {
  min(callback: (t: T) => number): [number, T | undefined]
  max(callback: (t: T) => number): [number, T | undefined]
}
