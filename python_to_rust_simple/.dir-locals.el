; -*- mode: Lisp -*-
(
(python-mode .
             (
              (eval . (venv--activate-dir (concat (projectile-project-root) "python_to_rust_simple/" "venv")))
              (mode . python-black-on-save)
              ;; (eval .(python-black-on-save-mode t)
              ;;(eval . (setq flycheck-checker 'python-mypy))
              ;;(eval . (setq flycheck-python-mypy-config "/Users/huseyin/GIVVA/recomendar/setup.cfg"))
              ))
 )
