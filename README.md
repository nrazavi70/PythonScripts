<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/uYcvrHX.png" alt="Project logo"></a>
</p>

<h3 align="center">CI/CD Vars TUI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This project helps create, delete, change and navigate thorough environmental variables in gitlab easier.

## 🏁 Getting Started <a name = "getting_started"></a>

In order to use this you can simply clone this repo and follow the instructions on the [deployment](#deployment) section and you are good to go.

### Prerequisites

The only requirement for this service to run is `python3` and python's `tabulate` library. Since python3 comes pre-installed on most linux flavours, you can just install `tabulate` via pip or apt and you can proceed to using this script. To install `tabulate` you can use one of the methods below:  

1. Via apt
```
sudo apt install python3-tabulate
```
2. Via pip
```
pip install tabulate
```
For this script to read and write data from [Gitlab](https://gitlab.com), you need an `access token` with `api_read` and `api` permissions. You can get this by:
1. Logging in to your gitlab account at [Gitlab](https://gitlab.com)
2. Clicking on your account's icon on the top right part of the page.
3. Selecting `Preferences` .
4. Navigating to the `Access Tokens` tab from the left menu.
5. Filling out the form and creating it.

### Installing

As explained in the [About](#about) section, you only have to clone the repo and run `GitlabVariables.py` file with python3.

```
git clone git@gitlab.ernyka.com:devops/cicd-python.git
cd cicd-python
python3 GitlabVariables.py
```

End with an example of getting some data out of the system or using it for a little demo.

## 🎈 Usage <a name="usage"></a>

1. When you run the script, you have to supply it with the token you created at [Prerequisites](#prerequisites) section. You are presented with the projects on which you have access. 
2. Here you can select your desired project by entering its name or the number next to it.
3. Then you are presented with a list of variables and choices about what you want to do with them. 
4. From here on you can just follow the instructions the script provides you on each step.

**Good Luck**

## ✍️ Authors <a name = "authors"></a>

- [@n.razavi](https://gitlab.ernyka.com/n.razavi) - Idea & Initial work
