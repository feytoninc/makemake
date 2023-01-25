const sec = 1000;
const min = sec * 60;
const hour = min * 60;
const day = hour * 24;

const end = new Date("Jan 30, 2023 12:00:00").getTime();

const int = setInterval(() => {
  const current = new Date().getTime();
  const remaining = end - current;
  document.getElementById("days").innerText = Math.floor(remaining / day);
  document.getElementById("hours").innerText = Math.floor(
    (remaining % day) / hour
  );
  document.getElementById("minutes").innerText = Math.floor(
    (remaining % hour) / min
  );
  document.getElementById("seconds").innerText = Math.floor(
    (remaining % min) / sec
  );

  if (remaining < 0) {
    document.querySelector(".message").innerText = "We Have Launched!";
    document.querySelector(".launch-msg").innerHTML =
      "The big day is finally here - view our <a href='https://makemake.rw'>Website<a/> for more information.";
    const digit = document.querySelectorAll("span");
    digit.forEach((digit) => {
      digit.innerText = "0";
    });
    clearInterval(int);
  }
}, 1000);
