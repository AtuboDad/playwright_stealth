const ua = navigator.userAgent

// const uaVersion = ua.includes('Chrome/')
//     ? ua.match(/Chrome\/([\d|.]+)/)[1]
//     : (await page.browser().version()).match(/\/([\d|.]+)/)[1]
const uaVersion = ua.match(/Chrome\/([\d|.]+)/)[1]

// Source in C++: https://source.chromium.org/chromium/chromium/src/+/master:components/embedder_support/user_agent_utils.cc;l=55-100
const _getBrands = () => {
  const seed = uaVersion.split('.')[0] // the major version number of Chrome

  const order = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0]
  ][seed % 6]
  const escapedChars = [' ', ' ', ';']

  const greaseyBrand = `${escapedChars[order[0]]}Not${
    escapedChars[order[1]]
  }A${escapedChars[order[2]]}Brand`

  const greasedBrandVersionList = []
  greasedBrandVersionList[order[0]] = {
    brand: greaseyBrand,
    version: '99'
  }
  greasedBrandVersionList[order[1]] = {
    brand: 'Chromium',
    version: seed
  }
  greasedBrandVersionList[order[2]] = {
    brand: 'Google Chrome',
    version: seed
  }

  return greasedBrandVersionList
}

const metadata = {
  platform: "macOSs",
  mobile: false,
  brands: _getBrands()
}

console.log("hi mike")

Object.defineProperty(Object.getPrototypeOf(navigator), 'userAgentData', {
    get: () => metadata
})
