/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{html,js}"
    ],
    theme: {
        extend: {
            fontFamily: {
                'montserrat': ['Montserrat'],
                'lato': ['Lato'],
                'garamond': ['Garamond']
            },
            colors: {
                "bg": "#272121",
                "bg-accent": "#443737",
                "bg-accent-dark": "#1B1B1B",
                "fg-accent": "#FF0000",
                "fg": "#FF4D00"
            }
        },
    },
    plugins: [],
}
