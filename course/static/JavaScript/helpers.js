String.prototype.format = function () {
	var formatted = unescape(this).replace('&amp;', '&');
	for (var i = 0; i < arguments.length; i++) {
		var regexp = new RegExp('\\{' + i + '\\}', 'gi');
		formatted = formatted.replace(regexp, arguments[i] ? arguments[i] : '');
	}
	return formatted;
};