// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx01;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

import rmiEx01.Servico;

public class Servidor {

	public static void main(String args[]) {
		try {
			String nomeServico = "MeuServico";
			int porta = 54321;

			Servico servico = new ImplementacaoServico();
			Servico servicoDistribuido = (Servico) UnicastRemoteObject.exportObject(servico, 0);

			Registry registry = LocateRegistry.createRegistry(porta);
			registry.bind(nomeServico, servicoDistribuido);
			System.out.printf("Servico disponivel: %s%n", nomeServico);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}