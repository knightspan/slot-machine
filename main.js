async function spin() {
    const bet = document.getElementById("bet").value;
    const lines = document.getElementById("lines").value;

    const res = await fetch("http://127.0.0.1:5000/spin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bet, lines })
    });

    const data = await res.json();
    const reels = data.slots;

    // Show each column (slot)
    reels.forEach((column, i) => {
        document.getElementById(`reel-${i}`).innerText = column.join(" | ");
    });

    document.getElementById("result").innerHTML = `
        🎉 You won $${data.winnings} <br>
        Winning lines: ${data.winning_lines.join(", ") || "None"}
    `;
}
