var key = 'AAAAZcj4Rbw:APA91bFK6p_oAAVMFlEUo3hfvdYY3pQS-8gTc3C8nkDl7OHRgsxMp3PDnkH7tY__tU1tKNXu-etFUGn9n_cOu5ElsSpw8x-Iy1j7Jxr9kgZgdZjRCXwB6bVXlyVkhqPAeNMyzPBEUDZF';
var to = 'BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k';
var notification = {
  'title': 'Portugal vs. Denmark',
  'body': '5 to 1',
};

fetch('https://fcm.googleapis.com/fcm/send', {
  'method': 'POST',
  'headers': {
    'Authorization': 'key=' + key,
    'Content-Type': 'application/json'
  },
  'body': JSON.stringify({
    'notification': notification,
    'to': to
  })
}).then(function(response) {
  console.log(response);
}).catch(function(error) {
  console.error(error);
})