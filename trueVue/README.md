# Welcome!

Thanks for getting the complete package! I hope you will find it useful.

If you would like to follow the book with the Companion App then follow these steps:

1 - Make sure you have Node.js installed.

2 - Go the Companion App project in your terminal

3 - Run `npm install` or `yarn` to install all dependencies

4 - Run `npm run serve` or `yarn serve` and enjoy!

Same steps apply to the Enterprise Boilerplate. 

## Beginners note

This book and resources are targeted at advanced developers and teams. If you have purchased this book, but are a beginner to web development, then I would strongly recommend going through some beginner materials first. Vue documentation is a great start:

- [Vue 2](https://vuejs.org/v2/guide/)
- [Vue 3](https://v3.vuejs.org/)

You might also want to read a few articles about what Node and NPM are.

- [What is Node](https://www.codecademy.com/articles/what-is-node)
- [Node.js Introduction](https://www.w3schools.com/nodejs/nodejs_intro.asp)
- [What is npm?](https://www.w3schools.com/whatis/whatis_npm.asp)
- [A Beginner's Guide to npm, the Node Package Manager](https://www.sitepoint.com/npm-guide/)

You should also get accustomed with using a Command Line Interface (Terminal)

-  [What is Command Line Interface (CLI)?](https://www.w3schools.com/whatis/whatis_cli.asp)

Try to go through guides for your specific OS, whether it is Window, Linux, or Mac. Without these pre-requisites, you might struggle with using and understanding the Companion App, Enterprise Boilerplate, and some of the examples in the book.

## Companion App note

Some customers run into an error below when trying to use the Companion App

```
npm ERR! code E401
npm ERR! Unable to authenticate, need: Basic realm="https://npm.fontawesome.com/%22,service=%22npm.fontawesome.com"
```

The Companion App is using a free set of Font Awesome icons. However, if you have previously used a PRO version of Font Awesome, then you might have the error above. If this is the case try this:

1. Run `npm config delete "@fortawesome:registry` command
2. Delete yarn/npm .lock files and node_modules directory, and install dependencies again

These steps should have fixed the issue.

## Contact

If you have any enquiries drop me an email at support@theroadtoenterprise.com.

##### 

