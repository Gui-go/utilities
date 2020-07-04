setTimeout(() => {
    console.log('in the timeout...')
    clearInterval(interval);
}, 3000)

const interval = setInterval(() => {
    console.log('in the interval')
}, 500)