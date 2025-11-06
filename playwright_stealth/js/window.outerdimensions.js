'use strict'

try {
    if (!!window.outerWidth && !!window.outerHeight) {
        const windowFrame = 85 // probably OS and WM dependent
        window.outerWidth = window.innerWidth
        window.outerHeight = window.innerHeight + windowFrame
    }
} catch (err) {
}
