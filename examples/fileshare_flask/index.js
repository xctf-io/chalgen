const puppeteer = require('puppeteer');

(async() => {

    const browser = await puppeteer.launch({
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--user-data-dir=/tmp/user'
        ]
    });

    const page = await browser.newPage();

    await page.setDefaultNavigationTimeout(5000)

    await page.goto('https://www.google.com/', {waitUntil: 'networkidle2'});
    await page.goto('https://www.duckduckgo.com/', {waitUntil: 'networkidle2'});
    await page.goto('https://www.facebook.com/', {waitUntil: 'networkidle2'});
    await page.goto('https://imgur.com/a/6pVCTsY' {waitUntil: 'networkidle2'});
    await page.goto('https://github.com/login')
    await page.type('#login_field', 'asdf')
    await page.type('#password', 'fdsa')
    await page.click('[name="commit"]')
    try {

      await page.waitForNavigation()
    } catch(e) {
    }

    const { exec } = require('child_process');
    exec('cp -r /tmp/user /app/history', (err, stdout, stderr) => {
    if (err) {
      console.error(err)
    } else {
      console.log(`stdout: ${stdout}`);
      console.log(`stderr: ${stderr}`);
    }

    browser.close();
});

})();