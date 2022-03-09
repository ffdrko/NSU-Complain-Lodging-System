const cls = document.querySelector('#cls');
const faq = document.querySelector('#faq');
const con = document.querySelector('#con');

cls.addEventListener('click', () => {
    cls.classList.add('active');
    faq.classList.remove('active');
    con.classList.remove('active');
})

faq.addEventListener('click', () => {
    faq.classList.add('active');
    cls.classList.remove('active');
    con.classList.remove('active');
})

con.addEventListener('click', () => {
    con.classList.add('active');
    faq.classList.remove('active');
    cls.classList.remove('active');
})
