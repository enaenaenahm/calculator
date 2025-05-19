document.getElementById('calculate').addEventListener('click', async () => {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;

    if (isNaN(num1) || isNaN(num2)) {
        alert("Введите корректные числа!");
        return;
    }

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ num1, num2, operation })
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById('result').textContent = "Ошибка: " + data.error;
        } else {
            document.getElementById('result').textContent = "Результат: " + data.result;
            updateHistory(data.history);
        }
    } catch (error) {
        console.error("Ошибка при отправке запроса:", error);
    }
});

function updateHistory(history) {
    const historyContainer = document.getElementById('history-content');
    historyContainer.innerHTML = '';

    for (let operation in history) {
        history[operation].forEach(entry => {
            const p = document.createElement('p');
            p.textContent = entry;
            historyContainer.appendChild(p);
        });
    }
}
