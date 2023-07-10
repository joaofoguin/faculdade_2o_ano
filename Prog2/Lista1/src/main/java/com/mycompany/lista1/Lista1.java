/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.lista1;

/**
 *
 * @author joaop
 */
public class Lista1 {

    public static void main(String[] args) {
    Lampada luz = new Lampada();
    luz.acender();
    luz.apagar();
    luz.mostrarEstado();

    Caixa box = new Caixa();
    box.largura = 3;
    box.altura = 2;
    box.profundidade = 3;
    System.out.println("Seu volume é de " + box.calcularVolume() + "cm3");

    Data dia1 = new Data ();
    System.out.println(dia1.formatarData("."));
    Data dia2 = new Data (2023);
    System.out.println(dia2.formatarData("/"));
    Data dia3 = new Data (10, 07, 2023);    
    System.out.println(dia3.formatarData("-"));
    }
}
