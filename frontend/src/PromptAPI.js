const api = process.env.REACT_APP_PROMPT_API_URL || 'http://localhost:8083'

let token = localStorage.token

if (!token)
  token = localStorage.token = Math.random().toString(36).substr(-8)

const headers = {
//  'Accept': 'application/json',
//  'Authorization': token
}

export const getAll = () =>
  fetch(`${api}/deltas`, { headers })
    .then(res => res.json())
    .then(data => data.deltas)

export const create = (body) =>
  fetch(`${api}/sentence`, {
    method: 'POST',
    headers: {
      ...headers,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }).then(res => res.json())
