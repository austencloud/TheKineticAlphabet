async function loadSVGs() {
    const response = await fetch("svg_paths.json");
    const svgPaths = await response.json();
    svgPaths.sort((a, b) => {
      const aNum = parseInt(a.match(/^\d+/));
      const bNum = parseInt(b.match(/^\d+/));
      return aNum - bNum;
    });
  
    for (let index = 0; index < svgPaths.length; index++) {
      await addSvg(svgPaths[index], index);
    }
  }
  
  

  function addSvg(svgPath, index) {
    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const iframe = document.createElement("iframe");
          iframe.classList.add("svg-iframe");
          iframe.width = "100%";
          iframe.style.border = "none";
          iframe.scrolling = "no"; // Disable scrolling for the iframe
          iframe.id = `svg-${index}`; // Set a unique ID for each iframe
          document.getElementById("main-doc").appendChild(iframe);
  
          const iframeDoc = iframe.contentWindow.document;
          iframeDoc.open();
          iframeDoc.write(xhr.responseText);
          iframeDoc.close();
  
          const svg = iframeDoc.querySelector("svg");
          svg.style.display = "block";
          svg.style.maxWidth = "60%";
          svg.style.height = "auto";
          const height = svg.getBoundingClientRect().height;
          iframe.height = height;
  
          addSidebarLink(index, iframeDoc, svgPath);
          resolve();
        }
      };
      xhr.onerror = function () {
        reject(new Error("Request failed."));
      };
      xhr.open("GET", svgPath, true);
      xhr.send();
    });
  }
  
  
  function cleanTitle(title) {
    const cleanedTitle = title.replace(/^\d+_-_/, '').replace(/_/g, ' ');
    return cleanedTitle;
  }
  
  function addSidebarLink(index, iframeDoc, svgPath) {
    const navbar = document.querySelector("#navbar .navbar-ul");
    const listItem = document.createElement("li");
    listItem.classList.add("navbar-li");
  
    const anchor = document.createElement("a");
    anchor.href = `#svg-${index}`;
    anchor.id = `nav-${index}`; // Set a unique ID for each navbar link
    anchor.classList.add("nav-link");
  
    // Use the cleaned-up file name as the link text
    const fileName = svgPath.split('/').pop().replace('.html', '');
    const linkText = cleanTitle(fileName);
  
    anchor.textContent = linkText;
  
    anchor.addEventListener("click", function () {
      document.title = linkText + " - The Kinetic Alphabet Guide";
    });
  
    listItem.appendChild(anchor);
    navbar.appendChild(listItem);
  }
  
  
document.addEventListener("DOMContentLoaded", function() {
    loadSVGs().then(() => {
        document.querySelector("#nav-0").click();
    });

});

