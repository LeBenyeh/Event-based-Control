.PHONY: run

run:
	python3 simulation.py

.PHONY: generate

generate:
	pyreverse -A -S \
		--colorized \
		-o png \
		-p convoyeur_system \
		--output-directory=Diagrams \
		Box.py \
		Collector.py \
		Conveyor.py \
		Corner.py \
		DetectionZone.py \
		Dispenser.py \
		Selector.py \
		Transformer.py \
		SelectorState.py \
		SectionType.py \
		assets.py \
		settings.py \
		simulation.py
