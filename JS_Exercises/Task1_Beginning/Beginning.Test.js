const { hello } = require ('./Beginning'); 

test('should output Hello World', () => {

    const text = hello();

    expect(text).toBe('Hello, World!');
    expect(hello()).toEqual('Hello, World!');
});
