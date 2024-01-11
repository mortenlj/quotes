<script>
  import '../app.scss';
</script>

<main class="text-center text-lg-start bg-body">
    <div class="container py-4">
        <h1 class="mb-3">Quotes</h1>
        <slot/>
    </div>
</main>

<!-- Footer -->
<footer class="text-center text-lg-start bg-body-tertiary text-muted py-3 my-4">
    <section class="">
        <div class="container text-center text-md-start">
            <!-- Grid row -->
            <div class="row mt-3">
                <!-- Grid column -->
                <!-- Section: Disclaimer  -->
                <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                    <!-- Content -->
                    <h6 class="text-uppercase fw-bold mb-4">
                        <i class="fas fa-gem me-3"></i>Disclaimer
                    </h6>
                    <p>
                        The quotes have varied sources, and are not necessarily attributed to the correct person, and
                        certainly not factually correct.
                    </p>
                </div>
                <!-- Section: Disclaimer  -->
                <!-- Grid column -->

                <!-- Grid column -->
                <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                    <!-- Links -->
                    <h6 class="text-uppercase fw-bold mb-4">
                        Links
                    </h6>
                    <p>
                        <a href="https://github.com/mortenlj/quotes" class="text-reset">Source</a>
                    </p>
                    <p>
                        <a href="https://github.com/mortenlj/quotes/issues" class="text-reset">Issue tracker</a>
                    </p>
                    <p>
                        <a href="/docs" class="text-reset">API documentation</a>
                    </p>
                </div>
                <!-- Grid column -->
            </div>
            <!-- Grid row -->
        </div>
    </section>

    <!-- Copyright -->
    <div class="text-center p-4 bg-body-secondary">
        © 2024 Copyright:
        <a class="text-reset fw-bold" href="https://home.ibidem.no/">Morten Lied Johansen</a>
    </div>
    <!-- Copyright -->
</footer>
<!-- Footer -->
