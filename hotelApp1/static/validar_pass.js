function check(input) {
    if (input.value != document.getElementById('password').value) {
        input.setCustomValidity('Los passwords deben ser iguales.');
    } else {
        // input is valid -- reset the error message
        input.setCustomValidity('');
    }
}