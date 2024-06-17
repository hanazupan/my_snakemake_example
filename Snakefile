rule hello_world:
  shell:
    'echo "Hello World!"'


rule generate_pt:
    input:
        config_file = "input/config_generate_pt/generate_pt_0001.yaml",
        m1_file = "input/H2O.gro"
    #output: "output/data/pt_files/H2O.txt", "output/figures/my_pic_H2O.pdf"
    #log: "scripts/logging/H2O.log"
    shell: 'python -m scripts.mock_generate_pt -m1 {input.m1_file} -m2 {input.m1_file} -b {input.config_file.b_grid} -o {input.o} -t {input.t}'