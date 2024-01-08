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
<footer class="text-center text-lg-start bg-body-tertiary text-muted">
    <!-- Section: Disclaimer  -->
    <section class="">
        <div class="container text-center text-md-start mt-5 p-4">
            <p>The quotes have varied sources, and are not necessarily attributed to the correct person, and certainly
                not factually correct.</p>
        </div>
    </section>
    <!-- Section: Disclaimer  -->

    <!-- Copyright -->
    <div class="text-center p-4 bg-body-secondary">
        © 2024 Copyright:
        <a class="text-reset fw-bold" href="https://home.ibidem.no/">Morten Lied Johansen</a>
    </div>
    <!-- Copyright -->
</footer>
<!-- Footer -->
