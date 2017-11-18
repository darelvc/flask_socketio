var socket = io.connect('http://192.168.0.102:5000/')

socket.on('connect', function() {
	socket.emit('my event', {
		data: 'User connected'
	})

})

var form = $('form').on('submit', function(e) {
	e.preventDefault()
	var user_name = $('input.username').val()
	var message = $('input.message').val()
	// console.log(user_name, message)
	socket.emit('my event', {
		user: user_name,
		msg: message
	})

	$('input.message').val('').focus()
})

socket.on('my response', function(msg) {
	if (typeof msg.user !== 'undefined') {
		$('h1').remove()
		$('div.msg-wrapper').append('<div class="msgbbl"><b>' + msg.user + ': </b>' + msg.msg + '</div>')
	}
	console.log(msg);
});