import { decodedValue } from './resistor-color-duo.ts'

describe('Resistor Colors', () => {
  it('Brown and black', () => {
    const result = decodedValue(['brown', 'black'])
    expect(decodedValue(['brown', 'black'])).toEqual(10)
    console.log(typeof result)
  })

  it('Blue and grey', () => {
    expect(decodedValue(['blue', 'grey'])).toEqual(68)
  })

  it('Yellow and violet', () => {
    expect(decodedValue(['yellow', 'violet'])).toEqual(47)
  })

  it('Orange and orange', () => {
    expect(decodedValue(['orange', 'orange'])).toEqual(33)
  })

  it('Ignore additional colors', () => {
    expect(decodedValue(['green', 'brown', 'orange'])).toEqual(51)
  })

})