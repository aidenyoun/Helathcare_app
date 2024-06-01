function submitSurvey() {
    let totalValue = 0;
    const questions = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10'];
    questions.forEach((question) => {
        const selected = document.querySelector(`input[name="${question}"]:checked`);
        if (selected) {
            totalValue += parseInt(selected.value);
        }
    });

    document.getElementById('total_value').value = totalValue;

    const form = document.getElementById('survey-form');
    const formData = new FormData(form);

    fetch('/checklist_main/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('final_result').innerText = data.result;
        document.getElementById('result').style.display = 'block';
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

