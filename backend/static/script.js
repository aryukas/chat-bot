function appendMessage(sender, message) {
    const chat = document.getElementById("chat");
    const msgDiv = document.createElement("div");
    msgDiv.className = sender === "Bot" ? "bot-message" : "user-message";
    msgDiv.innerText = message;
    chat.appendChild(msgDiv);
    chat.scrollTop = chat.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    appendMessage("You", message);

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        appendMessage("Bot", data.reply);
    } catch (err) {
        console.error(err);
        appendMessage("Bot", "Sorry, there was an error connecting to the server.");
    }

    input.value = "";
}
