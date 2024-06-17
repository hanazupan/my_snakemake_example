configfile: "config.yaml"

rule generate_pt:
    input: "input/H2O.gro"
    #output: "output/data/pt_files/H2O.txt", "output/figures/my_pic_H2O.pdf"
    #log: "scripts/logging/H2O.log"
    shell: 'python -m scripts.mock_generate_pt -m1 H2O -m2 H2O -b 17 -o 13 -t "linspace(0.2, 0.5, 20)"'