import { isLeap } from './leap'

describe('leap years', () => {
    it('leap is not', () => {
      expect(isLeap(2015)).toEqual(
        false
      )
    })
  
    it('leap', () => {
      expect(decodedResistorValue(1996)).toEqual(true)
    })
})