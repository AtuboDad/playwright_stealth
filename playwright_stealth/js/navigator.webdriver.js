Object.defineProperty(Object.getPrototypeOf(navigator), 'webdriver', {
    set: undefined,
    enumerable: true,
    configurable: true,
    get: new Proxy(
        Object.getOwnPropertyDescriptor(Object.getPrototypeOf(navigator), 'webdriver').get,
        { apply: (target, thisArg, args) => {
            // emulate getter call validation
            Reflect.apply(target, thisArg, args);
            return false;
        }}
    )
});