// replace Headless references in default useragent
const current_ua = navigator.userAgent
Object.defineProperty(Object.getPrototypeOf(navigator), 'userAgent', {
    get: () => window.opts.navigator_user_agent || current_ua.replace(/Headless/g, '')
})
