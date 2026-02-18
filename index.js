async function sendMessage() {

    let inputField = document.getElementById("userInput");
    let message = inputField.value;

    if (message.trim() === "") return;

    addMessage("You: " + message);

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();
        addMessage("Bot: " + data.reply);

    } catch (error) {
        addMessage("Bot: Server error. Please try again.");
    }

    inputField.value = "";
}

function addMessage(text) {
    let chatBox = document.getElementById("chatBox");

    let messageElement = document.createElement("p");
    messageElement.textContent = text;

    chatBox.appendChild(messageElement);

    chatBox.scrollTop = chatBox.scrollHeight;
}

