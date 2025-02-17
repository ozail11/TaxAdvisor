function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div><strong></strong> ${userInput}</div>`;

    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div><strong></strong> ${data.response}</div>`;
        document.getElementById("user-input").value = "";
    });
}
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("user-input").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});
function addMessage(message, sender) {
    let chatBox = document.getElementById("chat-box");
    let messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "message user-message";
    } else {
        messageDiv.className = "message bot-message";
    }

    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
    
    chatBox.scrollTop = chatBox.scrollHeight;
}

