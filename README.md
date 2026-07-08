# SigmaFold

**From Sequence to Structure: A Web-Based Gateway to AlphaFold**

SigmaFold is a browser-based application designed to improve access to AI-driven biology. By providing a seamless, visual interface to run **AlphaFold2** on the **Ohio Supercomputer Center (OSC)** servers, SigmaFold lowers the barrier to entry for protein structure prediction, reduces computing costs, and empowers the next generation of researchers to engage with High-Performance Computing (HPC) in a hands-on way. 

---

## An AI-Driven Future

Traditionally, running complex AI models like AlphaFold requires significant technical expertise, expensive hardware, and command-line proficiency. SigmaFold changes the status quo by acting as a bridge between the raw power of supercomputers and the aspiring scientists who need them. 

By simplifying access to OSC resources, SigmaFold:
* **Increases Accessibility:** No command-line experience required.
* **Lowers the Cost of Entry:** Utilizes existing OSC HPC infrastructure rather than requiring expensive local hardware.
* **Accelerates Discovery:** Helps users quickly turn biological ideas into structural realities.

---

## Key Features

* **Browser-Based Dashboard:** A clean, easy-to-navigate GUI accessible from anywhere.
* **Direct OSC Integration:** Seamlessly communicates with Ohio Supercomputer Center servers to handle the heavy lifting.
* **Visual Results:** View and interact with predicted 3D protein structures directly within the app.
* **Automated Job Management:** Handles job submission, queuing, and retrieval behind the scenes.

---

## How It Works

SigmaFold abstracts away the complexity of HPC job scheduling and container management. Here is the typical workflow:

1.  **Input:** The user inputs an amino acid sequence (FASTA format) into the SigmaFold web interface.
2.  **Translation & Submission:** The web app finds the full protein sequence from a database, translates the request, and securely submits the compute job to the OSC clusters.
3.  **HPC Processing:** OSC allocates the necessary GPU resources and runs the AlphaFold2 algorithm to predict the protein's 3D structure.
4.  **Retrieval & Visualization:** Once complete, SigmaFold fetches the output graphs (PDB format) from OSC and renders an interactive 3D model right in your browser.

---

## Recognition

SigmaFold was originally developed as a STEM Institute project aimed at demonstrating how quickly and effectively software can bridge the gap between users and high-performance computing. 

The impact of this project was recognized at the annual **Gateways Conference** in Green Bay, Wisconsin—a gathering of developers, researchers, and educators dedicated to advancing discovery through science gateways. The project was presented as a poster titled *“From Sequence to Structure: A Web-Based Gateway to AlphaFold Through Ohio Supercomputer Center Resources,”* showcasing how SigmaFold successfully lowers the barrier to exploring protein structure prediction for new users.

---

## SigmaFold: Building the future of accessible, AI-driven structural biology.

![Scientific Gateways 2025 Poster](Poster.png)
