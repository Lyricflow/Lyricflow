const keys = require("./keys");

module.exports = {
	localAPI: {
		url: "https://kind-elephant-52.localtunnel.me",
		headers: {
			Authorization: keys.genius
		},
		qs: {
			q: ""
		},
		json: true
	}
}