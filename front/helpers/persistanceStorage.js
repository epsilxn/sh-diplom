
export const getItem = key => {
    try {
        return JSON.parse(localStorage.getItem(key))
    } catch {
        return null
    }
}

export const setItem = (key, value) => {
    localStorage.setItem(key, JSON.stringify(value))
}

export const getString = key => {
    try {
        return String(JSON.parse(localStorage.getItem(key)))
    } catch {
        return null
    }
}


