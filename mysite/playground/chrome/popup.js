function callChatGPT() {
  const input = document.getElementById("user_input").value;
  fetch("<https://api.openai.com/v1/engines/davinci-codex/completions>", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer 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"
    },
    body: JSON.stringify({
      prompt: input,
      max_tokens: 50,
      n: 1,
      stop: "\\n"
    })
  })
  .then(response => response.json())
  .then(data => {
    const response = data.choices[0].text;
    document.getElementById("response").innerHTML = response;
  })
  .catch(error => console.error(error));
}
