const API_URL = window.location.hostname === "localhost"
  ? "http://localhost:5000/feedback"
  : "http://backend:5000/feedback";


async function sendFeedback() {
  const name = document.getElementById("name").value;
  const feedback = document.getElementById("feedback").value;

  if (!name || !feedback) {
    document.getElementById("message").innerText = "Fill all fields!";
    return;
  }

  await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({name, feedback})
  });

  document.getElementById("message").innerText = "Submitted!";
  loadFeedbacks();
}

async function loadFeedbacks() {
  const res = await fetch(API_URL);
  const data = await res.json();

  const list = document.getElementById("feedbackList");
  list.innerHTML = "";

  data.forEach(item => {
    const div = document.createElement("div");
    div.className = "feedback-item";
    div.innerHTML = `<strong>${item.name}</strong><p>${item.feedback}</p>`;
    list.appendChild(div);
  });
}

loadFeedbacks();
