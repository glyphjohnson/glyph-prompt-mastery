sed -i 's|<li><a href="cs.html">CS Pack</a></li>|<li><a href="cs.html">CS Pack</a></li>
            <li><a href="#newsfeed">News Feed</a></li>|g' index.html
sed -i '/<\/nav>/a \\
    <section id="header" style="background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); padding: 2rem 0; text-align: center; box-shadow: 0 4px 30px rgba(0,0,0,0.1);">
        <div class="container">
            <h1 style="font-size: clamp(2.5rem, 6vw, 5rem); font-weight: 800; background: linear-gradient(45deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.5rem; text-align: center;">Glyph Prompt Mastery 💼</h1>
            <p style="font-size: 1.4rem; opacity: 0.9; max-width: 500px; margin: 0 auto; text-align: center;">Master Prompt Engineering for E-Commerce Success</p>
        </div>
    </section>' index.html
sed -i '/<footer>/i \\
    <section id="newsfeed" style="padding: 5rem 0;">
        <div class="container">
            <h2 class="section-title">Prompt Engineering News Feed</h2>
            <div style="max-width: 600px; margin: 2rem auto; height: 800px; border-radius: 15px; overflow: hidden; box-shadow: 0 15px 40px rgba(0,0,0,0.1);">
                <a class="twitter-timeline" href="https://twitter.com/search?q=%23PromptEngineering&src=typed_query&f=live" data-height="800">Latest #PromptEngineering Tweets</a>
                <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            </div>
        </div>
    </section>' index.html
git add index.html
git commit -m 'add-header-newsfeed'
git push origin main
