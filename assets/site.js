// Publicador Videos: deslizador de fases, selector de marcas, cupón de contacto y entradas.
document.documentElement.classList.remove("no-js");
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

// Cómo funciona: un deslizador mueve la frase y el fragmento del terminal a la vez
const how = document.querySelector("[data-how]");
if (how) {
  const range = how.querySelector("input[type=range]");
  const stages = JSON.parse(how.querySelector("script[type='application/json']").textContent);
  const title = how.querySelector("[data-how-title]");
  const text = how.querySelector("[data-how-text]");
  const term = how.querySelector("[data-how-term]");
  const names = [...how.querySelectorAll(".stages li")];
  const show = (i) => {
    const s = stages[i];
    range.value = i;
    how.querySelector("[data-range]").style.setProperty("--p", `${(i / (stages.length - 1)) * 100}%`);
    range.setAttribute("aria-valuetext", s.name);
    names.forEach((li, j) => li.classList.toggle("on", j === i));
    const swap = () => {
      title.textContent = s.title;
      text.textContent = s.text;
      term.innerHTML = s.term;
      [title, text, term].forEach((el) => (el.style.opacity = 1));
    };
    if (reduce) return swap();
    [title, text, term].forEach((el) => (el.style.opacity = 0));
    setTimeout(swap, 200);
  };
  range.addEventListener("input", () => show(+range.value));
  names.forEach((li, j) => li.querySelector("button").addEventListener("click", () => show(j)));
}

// Las marcas: elegir un nombre cambia la imagen, el color de la forma y el dato
const brands = document.querySelector("[data-brands]");
if (brands) {
  const data = JSON.parse(brands.querySelector("script[type='application/json']").textContent);
  const img = brands.querySelector("[data-brand-img]");
  const disc = brands.querySelector(".brands__disc");
  const fact = brands.querySelector("[data-brand-fact]");
  const buttons = [...brands.querySelectorAll("[data-brand]")];
  const pick = (k) => {
    const b = data[k];
    buttons.forEach((btn) => btn.setAttribute("aria-pressed", btn.dataset.brand === k));
    disc.style.setProperty("--bc", b.colour);
    const swap = () => {
      img.src = b.img;
      img.alt = b.alt;
      fact.innerHTML = b.fact;
      img.style.opacity = 1;
    };
    if (reduce) return swap();
    img.style.opacity = 0;
    setTimeout(swap, 300);
  };
  buttons.forEach((btn) => {
    btn.addEventListener("click", () => pick(btn.dataset.brand));
    btn.addEventListener("mouseenter", () => matchMedia("(hover: hover)").matches && pick(btn.dataset.brand));
  });
}

// Contacto: sin servidor, prepara un correo con lo escrito
const form = document.querySelector("[data-mailto]");
if (form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const f = new FormData(form);
    const subject = `${form.dataset.subject} — ${f.get("topic")}`;
    const body = `${f.get("message")}\n\n${f.get("name")} <${f.get("email")}>`;
    location.href = `mailto:${form.dataset.mailto}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
}

// Entradas: cada parte de la sección sube con un pequeño retraso
const parts = document.querySelectorAll(".rise");
if ("IntersectionObserver" in window && !reduce) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) {
        en.target.classList.add("in");
        io.unobserve(en.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  parts.forEach((p) => io.observe(p));
} else {
  parts.forEach((p) => p.classList.add("in"));
}
