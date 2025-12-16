// Append message to chat area
function appendMessage(sender, message) {
    const chat = document.getElementById("chat");
    const msgDiv = document.createElement("p"); // using <p> for consistency
    msgDiv.className = sender === "Bot" ? "bot" : "user";
    msgDiv.textContent = message;
    chat.appendChild(msgDiv);
    chat.scrollTop = chat.scrollHeight;
}

// Send message function
async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    // Show user message
    appendMessage("You", message);
    input.value = "";

    try {
        // Call backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await response.json();

        // Show bot reply
        appendMessage("Bot", data.reply);
    } catch (err) {
        console.error(err);
        appendMessage("Bot", "Sorry, there was an error connecting to the server.");
    }
}

// Press Enter to send
document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
});
