const keys = require("./keys");

module.exports = {
	genius: {
		uri: "https://api.genius.com/search",
		headers: {
			Authorization: keys.genius
		},
		qs: {
			q: ""
		},
		json: true
	}
}