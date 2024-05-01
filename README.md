<p align="center"><img src="src/khoj/interface/web/assets/icons/khoj-logo-sideways-500.png" width="230" alt="Khoj Logo"></p>

<div align="center">

[![test](https://github.com/khoj-ai/khoj/actions/workflows/test.yml/badge.svg)](https://github.com/khoj-ai/khoj/actions/workflows/test.yml)
[![dockerize](https://github.com/khoj-ai/khoj/actions/workflows/dockerize.yml/badge.svg)](https://github.com/khoj-ai/khoj/pkgs/container/khoj)
[![pypi](https://github.com/khoj-ai/khoj/actions/workflows/pypi.yml/badge.svg)](https://pypi.org/project/khoj-assistant/)
![Discord](https://img.shields.io/discord/1112065956647284756?style=plastic&label=discord)

</div>

<div align="center">
<b>The open-source, personal AI for your digital brain</b>
</div>

<br />

<div align="center">

[🤖 Read Docs](https://docs.khoj.dev)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[🏮 Khoj Cloud](https://khoj.dev)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[💬 Get Involved](https://discord.gg/BDgyabRM6e)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[📚 Read Blog](https://blog.khoj.dev)

</div>

<div align="left">

***

Khoj is an application that creates always-available, personal AI agents for you to extend your capabilities.
- You can share your notes and documents to extend your digital brain.
- Your AI agents have access to the internet, allowing you to incorporate realtime information.
- Khoj is accessible on Desktop, Emacs, Obsidian, Web and Whatsapp.
- You can share pdf, markdown, org-mode, notion files and github repositories.
- You'll get fast, accurate semantic search on top of your docs.
- Your agents can create deeply personal images and understand your speech.
- Khoj is open-source, self-hostable. Always.

***

</div>

## See it in action

<img src="https://github.com/khoj-ai/khoj/blob/master/documentation/assets/img/using_khoj_for_studying.gif?raw=true" alt="Khoj Demo">

Go to https://app.khoj.dev to see Khoj live.

## Full feature list
You can see the full feature list [here](https://docs.khoj.dev/category/features).

## Self-Host

To get started with self-hosting Khoj, [read the docs](https://docs.khoj.dev/get-started/setup).

### How to use the deployment files [FDAi]
Stages of docker compose:
* local
* dev
* test x 2
  - `test.db`
      * Test a production database 
  - `test` 
      *   Using PgBouncer (Same as prod except for debug)
* prod
  - production ready if previous tests pass
  
General start-up command
```
sudo docker compose -f docker-compose.<stage>.yml up --build
```

## Contributors
Cheers to our awesome contributors! 🎉

<a href="https://github.com/khoj-ai/khoj/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=khoj-ai/khoj" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
