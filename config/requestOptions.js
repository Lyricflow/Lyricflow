const keys = require("./keys");

module.exports = {
	genius: {
		url: "api.genius.com/search",
		headers: {
			Authorization: keys.genius
		}
	}
}