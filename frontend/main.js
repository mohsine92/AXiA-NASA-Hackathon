document.addEventListener("DOMContentLoaded", async () => {
    const select = document.getElementById("planet-select");
    const descDiv = document.getElementById("planet-description");
  
    // Récupération des planètes
    const res = await fetch("/planets");
    const planets = await res.json();
  
    // Remplissage du menu déroulant
    planets.forEach(p => {
      const opt = document.createElement("option");
      opt.value = p.toi;
      opt.textContent = `Exoplanète ${p.toi}`;
      select.appendChild(opt);
    });
  
    // Gestion de la sélection
    select.addEventListener("change", async () => {
      const toi = select.value;
      if (!toi) {
        descDiv.textContent = "";
        return;
      }
  
      // Effet de chargement fluide
      const loadingMessages = [
        "🔭 Analyzing atmospheric data…",
        "🛰️ Cross-checking with NASA Exoplanet Archive…",
        "💫 Interpreting cosmic signals…",
        "🔭 Initializing AXiA analysis protocol...",
        "Retrieving stellar and orbital data from NASA archives...",
        "Parsing exoplanet parameters: radius, mass, temperature...",
        "Cross-checking with Kepler and TESS mission datasets...",
        "Estimating atmospheric composition...",
        "Detecting potential biosignatures (H₂O, O₂, CH₄)...",
        "Calculating surface gravity and equilibrium temperature...",
        "Evaluating stellar radiation impact...",
        "Running habitability index model...",
        "Compiling findings and generating summary..."
      ];
  
      descDiv.textContent = "";
      descDiv.style.opacity = "0";
  
      // Fonction pour afficher les messages un par un
      const showMessage = (msg, delay) => {
        return new Promise(resolve => {
          setTimeout(() => {
            descDiv.style.opacity = "0";
            setTimeout(() => {
              descDiv.textContent = msg;
              descDiv.style.transition = "opacity 0.8s ease";
              descDiv.style.opacity = "1";
            }, 300);
            resolve();
          }, delay);
        });
      };
  
      // Affiche les messages séquentiellement
      for (let i = 0; i < loadingMessages.length; i++) {
        await showMessage(loadingMessages[i], 1500);
      }
  
      // Récupère la vraie description ensuite
      try {
        const res = await fetch(`/description/${toi}`);
        const data = await res.json();
  
        // Transition douce vers la description finale
        descDiv.style.opacity = "0";
        setTimeout(() => {
          descDiv.textContent = data.description;
          descDiv.style.transition = "opacity 1s ease";
          descDiv.style.opacity = "1";
        }, 500);
  
      } catch (e) {
        descDiv.textContent = "⚠️ Erreur lors de la génération de la description.";
        console.error(e);
      }
    });
  });