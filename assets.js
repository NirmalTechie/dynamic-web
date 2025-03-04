class Assets {
    static loadImage(src) {
      return new Promise((resolve, reject) => {
        const img = new Image();
        img.src = src;
        img.onload = () => resolve(img);
        img.onerror = (err) => reject(err);
      });
    }
  
    static loadScript(src) {
      return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = src;
        script.onload = () => resolve(script);
        script.onerror = (err) => reject(err);
        document.head.appendChild(script);
      });
    }
  
    static loadStyle(href) {
      return new Promise((resolve, reject) => {
        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = href;
        link.onload = () => resolve(link);
        link.onerror = (err) => reject(err);
        document.head.appendChild(link);
      });
    }
  }
  
  // Example usage
  // Assets.loadImage('image.jpg').then(img => document.body.appendChild(img));
  // Assets.loadScript('script.js').then(() => console.log('Script loaded'));
  // Assets.loadStyle('style.css').then(() => console.log('Stylesheet loaded'));
  
  export default Assets;