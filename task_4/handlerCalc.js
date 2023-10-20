/**
 * Получает форму по её идентификатору и находит элементы ввода.
 *
 * @param {string} formId - Идентификатор формы.
 * @returns {Object} Объект, содержащий элементы ввода.
 */
const getFormInputs = (formId) => {
    const form = document.getElementById(formId);
    const input1 = form ? form.querySelector('input[name="digit1"]') : null;
    const input2 = form ? form.querySelector('input[name="digit2"]') : null;
    return { input1, input2 };
};

/**
 * Проверяет, является ли значение числом.
 *
 * @param {string} value - Значение для проверки.
 * @returns {boolean} `true`, если значение является числом, иначе `false`.
 */
const validateInput = (value) => !isNaN(parseFloat(value));

/**
 * Вычисляет сумму двух чисел.
 *
 * @param {number} num1 - Первое число.
 * @param {number} num2 - Второе число.
 * @returns {number} Сумма двух чисел.
 */
const calculateSum = (num1, num2) => num1 + num2;

/**
 * Обработчик события отправки формы.
 *
 * @param {Event} event - Объект события отправки формы.
 */
const handleSubmit = (event) => {
    event.preventDefault();

    const { input1, input2 } = getFormInputs("calculator");
    const resultSpan = document.getElementById("result");

    if (input1 && input2 && resultSpan) {
        const num1 = parseFloat(input1.value);
        const num2 = parseFloat(input2.value);

        if (validateInput(num1) && validateInput(num2)) {
            const sum = calculateSum(num1, num2);
            resultSpan.textContent = sum;
        } else {
            resultSpan.textContent = "Ошибка: Введите числа";
        }
    } else {
        console.error("Не удалось найти необходимые элементы на странице.");
    }
};

const form = document.getElementById("calculator");

if (form) {
    form.addEventListener("submit", handleSubmit);
}
